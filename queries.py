from article.models import Blog, Author, Entry
from datetime import date

Blog.objects.all().delete()
Author.objects.all().delete()
Entry.objects.all().delete()


b = Blog.objects.create(name = "Kittens", tagline = "Animals")
b2 = Blog.objects.create(name = "Pets", tagline = "Animalsiki")

a = Author.objects.create(name = "Nikitka", email = "123@456.xx")
a2 = Author.objects.create(name = "Mashutka", email = "vvv@hhh.xx")

e = Entry.objects.create(
    blog = b2,
    #blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = "Mypets",
    body_text = "",
    pub_date = date.today(),
    mod_date = date.today(),
    # authors = models.ManyToManyField(Author)
    n_comments = 0,
    n_pingbacks = 0,
    rating = 5,
)

e21 = Entry.objects.create(
    blog = b2,
    #blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = "Mypetits",
    body_text = "Mypetits",
    pub_date = date.today(),
    mod_date = date.today(),
    # authors = models.ManyToManyField(Author)
    n_comments = 1,
    n_pingbacks = 0,
    rating = 2,
)

print(Entry.objects.all())
print(Entry.objects.all())


