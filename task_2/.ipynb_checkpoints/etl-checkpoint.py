from api import APIRequests

class ETLProcesser():
    def __init__(self):
        self.earth_arr=[]
        self.air_date_arr=[]
        self.req = APIRequests()

    def earth_by_mounth(self):
        for i in range(1, TOTAL_EPISODS+1):
            episode = self.req.get_episode_json(str(i))
            earth_from_episode = 0
            air_date=episode['air_date']
            for i in range(len(episode['characters'])):
                character_origin_name = self.req.get_origin_name_of_character(episode['characters'][i])
                character_name = self.req.get_character_name(episode['characters'][i])
                if character_origin_name.find('Earth')!=-1:
                    earth_from_episode+=1
            self.earth_arr.append(earth_from_episode)
            self.air_date_arr.append(air_date)
        return [self.air_date_arr, self.earth_arr]