'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362
Description:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For more than 4 names, the number in and 2 others simply increases.
'''
def likes(names):
    string=""
    if not names:
        string="no one likes this"
    else:
        if len(names)==1:
            string=names[0] + " likes this"
        elif len(names)==2:
            string=names[0] + " and " + names[1] + " like this"
        elif len(names)==3:
            string=names[0] + ", " + names[1] +" and " + names[2]  +" like this"
        else:
            string=names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"
    return string