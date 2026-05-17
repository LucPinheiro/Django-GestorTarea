from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Tarea
from .forms import TareaForm
import csv
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def lista_tareas(request):

    estado = request.GET.get('estado')
    busqueda = request.GET.get('buscar')
    vista = request.GET.get('vista', 'kanban')

    tareas = Tarea.objects.all()

    # FILTROS
    if estado:
        tareas = tareas.filter(estado=estado)

    if busqueda:
        tareas = tareas.filter(titulo__icontains=busqueda)

    # ORDEN
    tareas = tareas.order_by('estado', 'id')

    # TOTAL
    total = tareas.count()

    # COLUMNAS KANBAN
    tareas_borrador = tareas.filter(estado='Borrador')
    tareas_pendientes = tareas.filter(estado='Pendiente')
    tareas_proceso = tareas.filter(estado='En proceso')
    tareas_completadas = tareas.filter(estado='Completada')

    # PAGINADOR
    paginator = Paginator(tareas, 10)

    page_number = request.GET.get('page')

    tareas = paginator.get_page(page_number)

    posicion = tareas.start_index() if total > 0 else 0
    page = request.GET.get("page", 1)

    vista = request.GET.get("vista", "kanban")
    seleccion = request.GET.get("seleccion")

    return render(request, 'tareas/lista.html', {

        'tareas': tareas,

        'tareas_borrador': tareas_borrador,
        'tareas_pendientes': tareas_pendientes,
        'tareas_proceso': tareas_proceso,
        'tareas_completadas': tareas_completadas,

        'estado': estado,
        'busqueda': busqueda,
        'vista': vista,

        'total': total,
        'posicion': posicion,
        "vista": vista,
        "page": page,
        "seleccion": seleccion,
    })


def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
            return redirect("detalle_tarea", id=tarea.id)
    else:
        form = TareaForm()


    return render(request, "tareas/detalle.html", {
        "form": form,
        "modo_formulario": True,
        "tarea": None,
    })




@login_required
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)

        if form.is_valid():
            tarea = form.save()
            messages.success(request, 'Tarea actualizada correctamente.')
            return redirect('detalle_tarea', id=tarea.id)

    else:
        form = TareaForm(instance=tarea)

    return render(request, 'tareas/detalle.html', {
        'form': form,
        'modo_formulario': True,
        'tarea': tarea,
    })


@login_required
def eliminar_tarea(request, id):

    tarea = get_object_or_404(Tarea, id=id)

    if request.method == 'POST':

        tarea.delete()

        messages.success(
            request,
            'Tarea eliminada correctamente.'
        )

        return redirect(
            f"{reverse('lista_tareas')}?vista=lista"
        )

    return render(
        request,
        'tareas/confirmar_eliminar.html',
        {'tarea': tarea}
    )

@login_required
def exportar_csv(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = (
        'attachment; filename="tareas.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
    'id',
    'titulo',
    'descripcion',
    'estado',
    'prioridad',
    'fecha_limite',
    'fecha_creada'
    ])

    # =========================================
    # EXPORTAR DESDE DETALLE
    # =========================================

    tarea_id = request.GET.get("tarea_id")

    if tarea_id:

        tareas = Tarea.objects.filter(
            id=tarea_id
        )

    else:

        # =========================================
        # EXPORTAR DESDE LISTA
        # =========================================

        ids = request.POST.getlist(
            "tareas_seleccionadas"
        )

        if ids:

            tareas = Tarea.objects.filter(
                id__in=ids
            ).order_by('estado')

        else:

            tareas = Tarea.objects.all().order_by(
                'estado'
            )

    # =========================================
    # GENERAR CSV
    # =========================================

    for tarea in tareas:

        writer.writerow([
            tarea.id,
            tarea.titulo,
            tarea.descripcion,
            tarea.estado,
            tarea.prioridad,
            tarea.fecha_limite,
            tarea.fecha_creada.date()
    ])

    return response

@login_required
def importar_csv(request):

    if request.method == 'POST':

        archivo = request.FILES.get('archivo_csv')

        if not archivo:
            messages.error(request, 'No has seleccionado ningún archivo.')
            return redirect('importar_csv')

        contenido = archivo.read()

        try:
            datos = contenido.decode('utf-8-sig').splitlines()
        except UnicodeDecodeError:
            datos = contenido.decode('latin-1').splitlines()

        lector = csv.DictReader(datos)

        importadas = 0
        omitidas = 0
        errores = 0

        for fila in lector:

            id_csv = fila.get('id')

            if id_csv and Tarea.objects.filter(id=id_csv).exists():
                omitidas += 1
                continue

            try:
                Tarea.objects.create(
                    titulo=fila.get('titulo', '').strip(),
                    descripcion=fila.get('descripcion', '').strip(),
                    estado=fila.get('estado') or 'Borrador',
                    prioridad=int(fila.get('prioridad') or 1),
                    fecha_limite=fila.get('fecha_limite') or None
                )

                importadas += 1

            except Exception:
                errores += 1

        if importadas:
            messages.success(
                request,
                f'Se importaron correctamente {importadas} tareas.'
            )
        else:
            messages.warning(
                request,
                f'No se importaron tareas nuevas porque ya existen en el sistema.'
            )

        return redirect('lista_tareas')

    return render(request, 'tareas/importar_csv.html')


@login_required
def detalle_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    vista = request.GET.get("vista", "kanban")
    page = request.GET.get("page", "1")
    seleccion = request.GET.get("seleccion", str(tarea.id))

    tareas = list(Tarea.objects.all().order_by('estado', 'id'))

    posicion = tareas.index(tarea) + 1
    total = len(tareas)

    anterior = tareas[posicion - 2] if posicion > 1 else None
    siguiente = tareas[posicion] if posicion < total else None

    return render(request, "tareas/detalle.html", {
        "tarea": tarea,
        "posicion": posicion,
        "total": total,
        "anterior": anterior,
        "siguiente": siguiente,
        "modo_formulario": False,
        "vista": vista,
        "page": page,
        "seleccion": seleccion,
    })

@login_required
def cambiar_estado_simple(request, id, estado):
    tarea = get_object_or_404(Tarea, id=id)

    tarea.estado = estado
    tarea.save()

    messages.success(
        request,
        'Estado actualizado correctamente.'
    )

    return redirect('detalle_tarea', id=id)





def eliminar_tareas_seleccionadas(request):

    if request.method == "POST":

        ids = request.POST.getlist("tareas_seleccionadas")

        cantidad = len(ids)

        Tarea.objects.filter(id__in=ids).delete()

        if cantidad == 1:
            messages.success(request, "Tarea eliminada correctamente")
        else:
            messages.success(request, "Tareas eliminadas correctamente")

    return redirect('/tareas/?vista=lista')

@login_required
def cambiar_prioridad(request, id, prioridad):
    tarea = get_object_or_404(Tarea, id=id)

    tarea.prioridad = prioridad
    tarea.save()

    return redirect('detalle_tarea', id=tarea.id)


