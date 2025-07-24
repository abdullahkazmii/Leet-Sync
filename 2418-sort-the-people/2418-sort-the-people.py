class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # peopleMap = {}
        # for name, height in zip(names, heights):
        #     peopleMap[name] = height
        
        # sorted_people = sorted(peopleMap.items(), key=lambda x:x[1], reverse = True)
        # print(sorted_people)
        # return [person[0] for person in sorted_people]

        name_height_pairs = list(zip(names, heights))
        sorted_pairs = sorted(name_height_pairs, key=lambda pair: pair[1], reverse=True)
        return [name for name, height in sorted_pairs]
        