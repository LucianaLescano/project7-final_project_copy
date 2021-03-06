from config.configuration import db, collection

# Functions to make queries to MongoDB to get the information
# that the users requests

######### 1º PART

# Skincare Routine

def cleanser_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    eight = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Cleanser'}]}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(3).sort('Rating', -1))
    return eight

def moist_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    nine = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Moisturizer'}]}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(3).sort('Rating', -1))
    return nine

def sun_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    ten = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Sunscreen & After Sun Care'}]}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(3).sort('Rating', -1))
    return ten

def ton_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    eleven = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Toner'}]}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(3).sort('Rating', -1))
    return eleven

def serum_skincare_routine(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    twelve = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Face Serum'}]}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(3).sort('Rating', -1))
    return twelve

# Skincare Routine URL

def cleanser_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    thirteen = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Cleanser'}]}, {'_id':0, 'Brand':0, 'Category':0, 'Skin_Type':0, 'Ingredients':0, 'Price':0, 'Rating':0}).limit(3).sort('Rating', -1))
    return thirteen

def moist_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    fourteen = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Moisturizer'}]}, {'_id':0, 'Brand':0, 'Category':0, 'Skin_Type':0, 'Ingredients':0, 'Price':0, 'Rating':0}).limit(3).sort('Rating', -1))
    return fourteen

def sun_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    fiveteen = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Sunscreen & After Sun Care'}]}, {'_id':0, 'Brand':0, 'Category':0, 'Skin_Type':0, 'Ingredients':0, 'Price':0, 'Rating':0}).limit(3).sort('Rating', -1))
    return fiveteen

def ton_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    sixteen = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Toner'}]}, {'_id':0, 'Brand':0, 'Category':0, 'Skin_Type':0, 'Ingredients':0, 'Price':0, 'Rating':0}).limit(3).sort('Rating', -1))
    return sixteen

def serum_skincare_routine_url(routine_skin_option_for_query, routine_money_option_for_query):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    seventeen = list(collection.find({"$and":[{'Skin_Type':routine_skin_option_for_query},{'Price':{"$lte":routine_money_option_for_query}}, {'Category':'Face Serum'}]}, {'_id':0, 'Brand':0, 'Category':0, 'Skin_Type':0, 'Ingredients':0, 'Price':0, 'Rating':0}).limit(3).sort('Rating', -1))
    return seventeen


######### 2º PART

# First list: Brand

def brand(brand_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the brand
    input = user's input
    output = dictionary
    '''
    one = list(collection.find({'Brand':brand_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(6).sort('Rating', -1))
    return one

# Second list: Multi-Brand

def multi_brand(multi_brand_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the brands
    input = user's input
    output = dictionary
    '''
    two = list(collection.find({'Brand':{"$in":multi_brand_option}}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return two

# Third list: Category

def category(category_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the product's category
    input = user's input
    output = dictionary
    '''
    three = list(collection.find({'Category':category_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return three

# Fourth list: Multi-Category

def multi_category(multi_category_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the product's categories
    input = user's input
    output = dictionary
    '''
    four = list(collection.find({'Category':{"$in":multi_category_option}}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return four

# Fifth list: Skin Type

def skin_type(skin_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the skin type
    input = user's input
    output = dictionary
    '''
    five = list(collection.find({'Skin_Type':skin_option}, {'_id':0, 'Ingredients':0, 'URL':0, 'Price':0}).limit(5).sort('Rating', -1))
    return five

# Sixth list: Money

def money(money_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the price
    input = user's input
    output = dictionary
    '''
    six = list(collection.find({'Price':{"$lte":money_option}}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(5))
    return six

# Seventh list: Rating

def rating(rating_option):
    '''
    Query that returns the brand, category, name, skin type and rating according to the rating
    input = user's input
    output = dictionary
    '''
    seven = list(collection.find({'Rating':rating_option}, {'_id':0, 'Ingredients':0, 'URL':0}).limit(5))
    return seven