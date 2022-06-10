from config import collection_names, color_schemes
from tools.collection import Collection
from tools.color import degree_correction, normalize_to_hundred

def check_scheme(model):
    if model == None:
        return [0], 'monochromatic'
    
    if model in color_schemes:
        return color_schemes[model], model
    else:
        raise ValueError(f'Wrong scheme name, given: {model}.\nUse {str([value for value in color_schemes.keys()])} or None for monochromatic scheme.')


class Scheme:
    def __init__(
        self,
        h: int,
        s: int = 50,
        l: int = 50,
        a=1,
        model: str = None,
        steps: int = 10
    ):
        self.h = degree_correction(h)
        self.s = normalize_to_hundred(s)
        self.l = normalize_to_hundred(l)
        self.a = a
        self.steps = steps
        self.scheme = check_scheme(model)[0]
        self.model = check_scheme(model)[1]
        self.collections = self.generate_collections()
 

    def generate_collections(self):

        collections = []

        for s in self.scheme:
            name = collection_names['styling'][self.scheme.index(s)]
            collection = Collection(name, self.h + s, self.s, self.l, steps=self.steps)
            collections.append(collection)

        # check self.h half to determine if it is warm or cool; 
        # 345 + 180 == warm
        # 345 - 180 == cool

        hue_is_cool = 165 <=  self.h < 345

        warm = 0
        cool = 0

        if hue_is_cool:
            cool = self.h
            warm = self.h-180
        else:
            cool = self.h-180
            warm = self.h

        gray_saturation = 5

        gray_collection = Collection(collection_names['gray'][0], 0, 0, steps=self.steps)
        gray_warm_collection = Collection(collection_names['gray'][1], warm, gray_saturation, steps=self.steps)
        gray_cool_collection = Collection(collection_names['gray'][2], cool, gray_saturation, steps=self.steps)

        collections.append(gray_collection)
        collections.append(gray_cool_collection)
        collections.append(gray_warm_collection)

        nofification_collection = Collection(collection_names['ui'][0], h=self.h - 37, s=self.s, steps=self.steps)
        warning_collection = Collection(collection_names['ui'][1], h=self.h + 37, s=self.s, steps=self.steps)
        
        collections.append(nofification_collection)
        collections.append(warning_collection)

        return collections