from .models import Army


class GameActions:

    def attack_check_OK(self, obj_atack, obj_defend):
        if type(obj_defend) == Army:
            return False
        if type(obj_atack) == Army:
            if obj_defend.alive:
                return True
            else:
                return False
        else:
            if obj_atack.alive:
                if obj_defend.alive:
                    return True
                else:
                    return False
            else:
                return False
