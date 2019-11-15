# **kwargs is used for the contain all the key and the value
#  it returns the dictionary


def colors(**kwargs):
    for name,color in kwargs.items():
        print(f"{name}'s fav. color is  {color}");


colors(hiten="white",om="orange",aarvee="green")