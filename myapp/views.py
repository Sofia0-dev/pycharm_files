from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def products(request):
    age = 65
    weight = 71.85
    subjects = ["maths", "science", "engineering"]
    isDisabled = True
    name = "heha movers"

    data = {
        'miaka': age,
        'uzito': weight,
        'subjects': subjects,
        'isDisabled': isDisabled,
        'jina': name
    }
    return render(request, 'products.html', data)


def about(request):
    return render(request, 'about.html')


def students(request):
    scores = [
        {
            "name": "Hilel Franklin",
            "email": "et.rutrum.eu@yahoo.couk",
            "score": 74,
            "age": 18
        },
        {
            "name": "Jasper Morton",
            "email": "magna.et@google.edu",
            "score": 69,
            "age": 18
        },
        {
            "name": "Raja Johnson",
            "email": "elit.pretium@protonmail.couk",
            "score": 80,
            "age": 25
        },
        {
            "name": "Erasmus Lynn",
            "email": "sed.est@yahoo.couk",
            "score": 21,
            "age": 22
        },
        {
            "name": "Eaton Burris",
            "email": "pede.cras@yahoo.edu",
            "score": 54,
            "age": 23
        },
        {
            "name": "Quamar French",
            "email": "sapien.molestie.orci@outlook.org",
            "score": 21,
            "age": 22
        },
        {
            "name": "Amos Holman",
            "email": "massa.mauris@protonmail.couk",
            "score": 44,
            "age": 22
        },
        {
            "name": "Carter Brown",
            "email": "risus.morbi@google.ca",
            "score": 46,
            "age": 20
        },
        {
            "name": "Christopher Oneal",
            "email": "in.condimentum@hotmail.com",
            "score": 78,
            "age": 22
        },
        {
            "name": "Jackson Bryant",
            "email": "faucibus@google.net",
            "score": 53,
            "age": 25
        },
        {
            "name": "Kato Montoya",
            "email": "aliquam.tincidunt@google.org",
            "score": 22,
            "age": 20
        },
        {
            "name": "Conan Sweeney",
            "email": "mauris.blandit.enim@google.edu",
            "score": 64,
            "age": 18
        },
        {
            "name": "Oscar Buck",
            "email": "ut.molestie@aol.net",
            "score": 61,
            "age": 21
        },
        {
            "name": "Linus Malone",
            "email": "erat.sed@hotmail.edu",
            "score": 52,
            "age": 24
        },
        {
            "name": "Hyatt Francis",
            "email": "adipiscing.elit@aol.org",
            "score": 25,
            "age": 21
        },
        {
            "name": "Thor Ewing",
            "email": "orci.luctus@outlook.couk",
            "score": 56,
            "age": 23
        },
        {
            "name": "Boris Whitley",
            "email": "sed.malesuada@yahoo.net",
            "score": 55,
            "age": 24
        },
        {
            "name": "Clinton Moreno",
            "email": "quis.accumsan.convallis@hotmail.edu",
            "score": 70,
            "age": 20
        },
        {
            "name": "Aidan Moses",
            "email": "nec.euismod@protonmail.com",
            "score": 36,
            "age": 20
        },
        {
            "name": "Kirk Garrison",
            "email": "est.ac@google.org",
            "score": 26,
            "age": 22
        },
        {
            "name": "Paul Sheppard",
            "email": "tempus.non.lacinia@icloud.ca",
            "score": 41,
            "age": 19
        },
        {
            "name": "Kasper Koch",
            "email": "morbi.metus@google.net",
            "score": 94,
            "age": 18
        },
        {
            "name": "Dolan Hoffman",
            "email": "netus.et@icloud.ca",
            "score": 39,
            "age": 24
        },
        {
            "name": "Bernard Crawford",
            "email": "ligula.eu.enim@google.org",
            "score": 82,
            "age": 24
        },
        {
            "name": "Marshall Hopkins",
            "email": "tincidunt@google.net",
            "score": 76,
            "age": 20
        },
        {
            "name": "Hayes Fleming",
            "email": "elementum.lorem@google.edu",
            "score": 87,
            "age": 18
        },
        {
            "name": "George Sweet",
            "email": "id.mollis.nec@aol.org",
            "score": 70,
            "age": 20
        },
        {
            "name": "Arthur Cross",
            "email": "quisque.libero@google.edu",
            "score": 73,
            "age": 24
        },
        {
            "name": "Carl Ayala",
            "email": "suspendisse.eleifend@aol.edu",
            "score": 24,
            "age": 24
        },
        {
            "name": "Benedict Hall",
            "email": "magna.ut@outlook.ca",
            "score": 22,
            "age": 21
        },
        {
            "name": "Laith Mercer",
            "email": "enim.curabitur@yahoo.couk",
            "score": 63,
            "age": 22
        },
        {
            "name": "Camden Ratliff",
            "email": "tellus.nunc.lectus@yahoo.com",
            "score": 98,
            "age": 19
        },
        {
            "name": "Isaac Velazquez",
            "email": "rutrum.justo@google.net",
            "score": 34,
            "age": 21
        },
        {
            "name": "Rooney Pratt",
            "email": "turpis.nec@outlook.org",
            "score": 73,
            "age": 24
        },
        {
            "name": "Lee Stark",
            "email": "pretium@protonmail.org",
            "score": 49,
            "age": 22
        },
        {
            "name": "Caldwell Cash",
            "email": "nulla.tincidunt@protonmail.ca",
            "score": 31,
            "age": 25
        },
        {
            "name": "Sawyer Oneil",
            "email": "quis.massa@yahoo.ca",
            "score": 99,
            "age": 18
        },
        {
            "name": "Elliott Leonard",
            "email": "ornare.egestas@outlook.edu",
            "score": 58,
            "age": 25
        },
        {
            "name": "Chester Dunn",
            "email": "iaculis.odio@hotmail.couk",
            "score": 24,
            "age": 21
        },
        {
            "name": "Wallace Caldwell",
            "email": "eleifend.nunc@google.ca",
            "score": 78,
            "age": 22
        },
        {
            "name": "Jason Lester",
            "email": "phasellus@protonmail.ca",
            "score": 39,
            "age": 21
        },
        {
            "name": "Kenyon Briggs",
            "email": "rhoncus.nullam.velit@icloud.net",
            "score": 25,
            "age": 25
        },
        {
            "name": "Fritz Mccarthy",
            "email": "sed.congue@yahoo.com",
            "score": 81,
            "age": 24
        },
        {
            "name": "Paul Chan",
            "email": "sollicitudin.orci.sem@yahoo.couk",
            "score": 37,
            "age": 19
        },
        {
            "name": "Zeph Bruce",
            "email": "ultrices.sit@hotmail.org",
            "score": 53,
            "age": 21
        },
        {
            "name": "Edward Valenzuela",
            "email": "mauris.non@aol.net",
            "score": 38,
            "age": 19
        },
        {
            "name": "Hilel Boyle",
            "email": "at.augue@hotmail.edu",
            "score": 26,
            "age": 23
        },
        {
            "name": "Marsden Pollard",
            "email": "eu.ligula@google.com",
            "score": 31,
            "age": 24
        },
        {
            "name": "Zachery Duffy",
            "email": "mauris.sagittis.placerat@outlook.net",
            "score": 38,
            "age": 22
        },
        {
            "name": "Clark Rowland",
            "email": "ullamcorper.nisl@aol.edu",
            "score": 52,
            "age": 22
        },
        {
            "name": "Mannix Knapp",
            "email": "lacinia.orci@google.ca",
            "score": 77,
            "age": 24
        },
        {
            "name": "Levi Hernandez",
            "email": "ipsum.primis@aol.edu",
            "score": 48,
            "age": 19
        },
        {
            "name": "Jerome Garza",
            "email": "amet.diam@aol.net",
            "score": 92,
            "age": 20
        },
        {
            "name": "Ferris Mcknight",
            "email": "molestie@yahoo.net",
            "score": 35,
            "age": 21
        },
        {
            "name": "Ferris Pennington",
            "email": "libero.proin@outlook.couk",
            "score": 52,
            "age": 22
        },
        {
            "name": "Ulysses Middleton",
            "email": "aliquam.fringilla@hotmail.ca",
            "score": 95,
            "age": 23
        },
        {
            "name": "Coby Campbell",
            "email": "sem.pellentesque@protonmail.couk",
            "score": 95,
            "age": 21
        },
        {
            "name": "Perry Beck",
            "email": "in.ornare@icloud.edu",
            "score": 33,
            "age": 22
        },
        {
            "name": "Emery Schmidt",
            "email": "ligula@yahoo.org",
            "score": 88,
            "age": 19
        },
        {
            "name": "Lewis Mclean",
            "email": "senectus@google.org",
            "score": 40,
            "age": 25
        },
        {
            "name": "Dalton Cannon",
            "email": "magna.lorem@yahoo.edu",
            "score": 89,
            "age": 21
        },
        {
            "name": "Emerson Hogan",
            "email": "risus@icloud.edu",
            "score": 55,
            "age": 23
        },
        {
            "name": "Alexander Casey",
            "email": "mi@yahoo.com",
            "score": 51,
            "age": 22
        },
        {
            "name": "Graham Sandoval",
            "email": "ac.feugiat@yahoo.edu",
            "score": 24,
            "age": 23
        },
        {
            "name": "Chandler Fowler",
            "email": "orci.lacus.vestibulum@protonmail.ca",
            "score": 42,
            "age": 21
        },
        {
            "name": "Wesley Golden",
            "email": "tempus@icloud.ca",
            "score": 24,
            "age": 19
        },
        {
            "name": "Nicholas Bryan",
            "email": "orci.ut.sagittis@google.com",
            "score": 35,
            "age": 19
        },
        {
            "name": "Kenneth Villarreal",
            "email": "est@icloud.org",
            "score": 94,
            "age": 19
        },
        {
            "name": "Armando Lamb",
            "email": "lectus.pede.ultrices@yahoo.org",
            "score": 83,
            "age": 19
        },
        {
            "name": "Kasimir Cantrell",
            "email": "dui.nec@aol.edu",
            "score": 92,
            "age": 22
        },
        {
            "name": "Alfonso Case",
            "email": "sapien@outlook.couk",
            "score": 32,
            "age": 22
        },
        {
            "name": "Caldwell Kline",
            "email": "elit.pede@hotmail.com",
            "score": 98,
            "age": 19
        },
        {
            "name": "Jamal Allen",
            "email": "in.faucibus@aol.couk",
            "score": 36,
            "age": 19
        },
        {
            "name": "Chaney Marquez",
            "email": "nec.mollis.vitae@google.org",
            "score": 46,
            "age": 25
        },
        {
            "name": "Lucas Glover",
            "email": "integer@icloud.edu",
            "score": 79,
            "age": 22
        },
        {
            "name": "Addison Decker",
            "email": "sapien.gravida@google.net",
            "score": 98,
            "age": 18
        },
        {
            "name": "Ulric Gomez",
            "email": "vestibulum.ante@outlook.net",
            "score": 58,
            "age": 22
        },
        {
            "name": "Xanthus Merrill",
            "email": "consectetuer.adipiscing@outlook.net",
            "score": 20,
            "age": 23
        },
        {
            "name": "Acton Castro",
            "email": "risus.in@outlook.net",
            "score": 86,
            "age": 19
        },
        {
            "name": "Garrison Clements",
            "email": "enim.curabitur.massa@outlook.org",
            "score": 24,
            "age": 23
        },
        {
            "name": "Abraham Mcdaniel",
            "email": "non.egestas.a@hotmail.com",
            "score": 47,
            "age": 19
        },
        {
            "name": "Alan Benson",
            "email": "aenean.eget.metus@outlook.com",
            "score": 57,
            "age": 18
        },
        {
            "name": "Amir Mcbride",
            "email": "pede.praesent@aol.org",
            "score": 40,
            "age": 22
        },
        {
            "name": "Theodore Hinton",
            "email": "est.mollis@hotmail.ca",
            "score": 35,
            "age": 24
        },
        {
            "name": "Hedley Oliver",
            "email": "mauris@icloud.couk",
            "score": 27,
            "age": 25
        },
        {
            "name": "Boris Rosa",
            "email": "scelerisque.sed.sapien@hotmail.net",
            "score": 89,
            "age": 18
        },
        {
            "name": "Nash Willis",
            "email": "habitant.morbi@icloud.ca",
            "score": 57,
            "age": 19
        },
        {
            "name": "Phillip Rocha",
            "email": "ultricies@outlook.edu",
            "score": 84,
            "age": 20
        },
        {
            "name": "Ivan Everett",
            "email": "sed.pede@google.edu",
            "score": 44,
            "age": 24
        },
        {
            "name": "Solomon Flynn",
            "email": "turpis.non.enim@aol.com",
            "score": 75,
            "age": 22
        },
        {
            "name": "Travis Sellers",
            "email": "tincidunt@protonmail.com",
            "score": 21,
            "age": 19
        },
        {
            "name": "Guy Greene",
            "email": "egestas.sed@yahoo.net",
            "score": 66,
            "age": 25
        },
        {
            "name": "Kamal Fry",
            "email": "pede@hotmail.com",
            "score": 51,
            "age": 24
        },
        {
            "name": "Kermit Small",
            "email": "donec.egestas@outlook.org",
            "score": 45,
            "age": 24
        },
        {
            "name": "Finn Noel",
            "email": "purus.ac@yahoo.ca",
            "score": 27,
            "age": 20
        },
        {
            "name": "Fulton Lindsey",
            "email": "amet.orci@google.com",
            "score": 39,
            "age": 20
        },
        {
            "name": "Fritz Lewis",
            "email": "cursus.in.hendrerit@protonmail.edu",
            "score": 51,
            "age": 22
        },
        {
            "name": "Kirk Parsons",
            "email": "nascetur.ridiculus@outlook.net",
            "score": 97,
            "age": 23
        },
        {
            "name": "Guy Mcgee",
            "email": "nam@google.couk",
            "score": 92,
            "age": 19
        },
        {
            "name": "Kadeem Schwartz",
            "email": "tempor.diam@yahoo.org",
            "score": 97,
            "age": 21
        }
    ]
	data = {"students": scores}
    return render(request, 'students.html', data)

