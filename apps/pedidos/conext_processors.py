def carrito_context(request):
    "permite acceder al numero de figuraen el carrito desde cualquier plantilla"
    carrito = request.session.get("carrito",{})
    total_item= sum(item.get("cantidad",0) for item in carrito.values())
    return{
        "carrito_total_items":total_item
    }