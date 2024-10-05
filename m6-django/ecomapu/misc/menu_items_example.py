# Import the necessary modules
from menu.models import MenuItem

# Create a MenuItem entry for a hot drink
item1 = MenuItem(
    name="Café Espresso",
    description="Café fuerte y concentrado.",
    price=2500,
    category=MenuItem.Category.BEBIDA_CALIENTE,
    image="images/cafe_espresso.png"
)
item1.save()

# Create a MenuItem entry for a cold drink
item2 = MenuItem(
    name="Frappuccino de Caramelo",
    description="Bebida fría con café, leche, hielo y caramelo.",
    price=4500,
    category=MenuItem.Category.BEBIDA_FRIA,
    image="images/frappuccino_caramelo.png"
)
item2.save()

# Create a MenuItem entry for a dessert
item3 = MenuItem(
    name="Tarta de Queso",
    description="Deliciosa tarta de queso con base de galleta.",
    price=3800,
    category=MenuItem.Category.POSTRE,
    image="images/tarta_queso.png"
)
item3.save()