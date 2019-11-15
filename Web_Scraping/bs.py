from bs4 import BeautifulSoup

html="""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css" type="text/css">
    <title>My First Blog Post</title>
</head>

<body>
    <div class="container">
        <div class="blog-post">

            <h1>My first blog post</h1>
            <p class="date">19th May 1999</p>
            <h2>This is my first blog post</h2>
            <p class="main-text">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Omnis, rerum odit! Maiores quis rem possimus
                obcaecati fuga minima dolore labore adipisci. Nihil pariatur nam fugiat repellendus nisi obcaecati
                magni
                dolor
                tempora quisquam excepturi perspiciatis ad dolores quas, quos omnis? Obcaecati tempora totam
                consequuntur
                numquam nobis!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam quae, rerum iste delectus
                voluptas quos veritatis? Porro rem odio dolor ex sit non ea, sequi velit quia iste debitis. Ab itaque
                tempore
                quae quas porro cumque fugiat voluptas odio, repudiandae at corporis beatae alias voluptates eos
                eligendi
                tenetur mollitia id dolorum nisi incidunt eum blanditiis.</p>


            <a href="https://www.google.com" target="_blank">Google Link</a>
            <a href="logo1.jpg" target="_blank">HTML Logo</a>

            <h2 id="demo">HTML is amazing</h2>
            <p class="main-text">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam quae, rerum iste
                delectus
                voluptas quos
                veritatis? Porro rem odio dolor ex sit non ea, sequi velit quia iste debitis. Ab itaque tempore quae
                quas
                porro
                cumque fugiat voluptas odio, repudiandae at corporis beatae alias voluptates eos eligendi tenetur
                mollitia
                id
                dolorum nisi incidunt eum blanditiis.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam
                quae,
                rerum iste delectus voluptas quos veritatis? Porro rem odio dolor ex sit non ea, sequi velit quia iste
                debitis.
                Ab itaque tempore quae quas porro cumque fugiat voluptas odio, repudiandae at corporis beatae alias
                voluptates
                eos eligendi tenetur mollitia id dolorum nisi incidunt eum blanditiis.</p>
            <img src="logo1.jpg" alt="html 5 and css image">

        </div>
        <div class="other-post">
            <div class="other">
                This is the post About javaScript
            </div>
            <div class="other">
                This is the post About NodeJs
            </div>
            <div class="other">
                This is the post About Java
            </div>
        </div>

        <div class="clearfix"></div>

        <div class="author-box">
            <img src="author.jpg" alt="jon snow image">
            <p class="author-text">~Jon Snow(GOT)</p>
        </div>
    </div>

</body>

</html>

"""


soup = BeautifulSoup(html,"html.parser")
# print(soup)
# print(type(soup))
# print(soup.body)
# print(soup.body.div)
# print(soup.find("h1"))
# d =soup.find_all("h2")
# print(d)
# print(type(d))


# Example of the HTML TECHNIQUE

# Select the all the element which class name is the other

# print(soup.find_all(class_ = "other"))

# Select the data using the attribute
# alt="html 5 and css image"

# print(soup.find_all(attrs={"alt":"html 5 and css image"}))
# print(soup.find_all("img"))


# DATA SELECT USING THE CSS ATTR
# IT GIVES THE LIST

# print(soup.select(".other"))
# print(soup.select(".other")[0])
# print(soup.select(".other")[1])

# print(soup.select("#demo"))
# print(soup.select("#demo")[0])


# print(soup.select("[alt]"))