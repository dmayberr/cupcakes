from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="vanilla",
    size="large",
    rating=8.5,
    image="https://www.glorioustreats.com/wp-content/uploads/2011/07/perfect-vanilla-cupcakes-square.jpg"
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=8,
    image="https://cdn.sallysbakingaddiction.com/wp-content/uploads/2017/06/moist-chocolate-cupcakes-5.jpg"
)

c3 = Cupcake(
    flavor="Oreo",
    size="large",
    rating=5,
    image="https://www.tasteofhome.com/wp-content/uploads/2019/12/Oreo-Cupcakes-with-Cookies-and-Cream-Frosting_EXPS_FT19_247265_F_1203_1.jpg"
)

c4 = Cupcake(
    flavor="lemon",
    size="large",
    rating=9.5,
    image="https://i2.wp.com/lifemadesimplebakes.com/wp-content/uploads/2017/05/Lemon-Cupcakes-with-Lemon-Cream-Cheese-Frosting.jpg"
)

c5 = Cupcake(
    flavor="red velvet",
    size="small",
    rating=6.5,
    image="https://www.yourcupofcake.com/wp-content/uploads/2013/01/Red-Velvet-Cupcakes.jpg"
)



db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()