from django.shortcuts import render


def home(request):

    """_____I imported OrderedDict and created an instance of a dictionary of the Deck.Category choices
    _____It sorts by the id # so I had to call lambda function and key[1] is used because the keywords 
    _____are in that column. So basically this is how to sort your items by the category choices defined
    _____in the model's category dictionary.

    """



    return render(request, 'base.html')