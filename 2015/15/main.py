








# Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
# Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
# Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
# Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1


frosting = {'capacity':4, 'durability':-2, 'flavor':0, 'texture':0, 'calories':5}
candy = {'capacity':0, 'durability':5, 'flavor':-1, 'texture':0, 'calories':8}
butterscotch = {'capacity':-1, 'durability':0, 'flavor':5, 'texture':0, 'calories':6}
sugar = {'capacity':0, 'durability':0, 'flavor':-2, 'texture':2, 'calories':1}


ingredients = [frosting, candy, butterscotch, sugar]
properties = ['capacity', 'durability', 'flavor', 'texture', 'calories']





ports = []
count = 0
for i in range(100, -1, -1):
    jmax = 100-i

    for j in range( jmax, -1, -1):
        kmax = jmax -j

        for k in range(kmax, -1, -1):
            lmax = kmax-k

            for l in range(lmax, -1, -1):

                if i+j+k+l ==100:
                    ports.append( (i,j,k,l) )
                    count +=1



class Recipe:

    def __init__(self, portions, ):
        self.portions = portions

        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0

        for ingredient, portion in zip(ingredients, portions):
            self.capacity += ingredient['capacity']*portion
            self.durability += ingredient['durability']*portion
            self.flavor += ingredient['flavor']*portion
            self.texture += ingredient['texture']*portion
            self.calories += ingredient['calories']*portion


        self.capacity = max(0, self.capacity)
        self.durability = max(0, self.durability)
        self.flavor = max(0, self.flavor)
        self.texture = max(0, self.texture)

        self.score = self.capacity*self.durability*self.flavor*self.texture








max_score = 0
max_score_cal_cond = 0
for port in ports:

    r = Recipe(port)


    if r.score >max_score:
        max_score = r.score

    if r.score > max_score_cal_cond and r.calories ==500:
        max_score_cal_cond = r.score

print('Maximum score:')
print(max_score)

print('Maximum score with 500 calorie condition:')
print(max_score_cal_cond)







