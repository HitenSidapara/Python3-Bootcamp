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


soup =BeautifulSoup(html,"html.parser")

# for data in soup.find_all("div"):
#     # print(data.name)
#     # print(data.get_text())
#     # print(data.attr)
#     pass


# for data in soup.select(".other"):
#     print(data.get_text())
#     print(data.name)
#     print(data.attr)