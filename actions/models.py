from django.db import models


class ScoreAbstract(models.Model):

    damage = models.IntegerField(default=20, blank=False, null=False)
    lives = models.IntegerField(default=100, blank=False, null=False)
    alive = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return f"Id: {self.id}"

    class Meta:
        abstract = True

    @property
    def dead(self):
        self.lives = 0
        self.damage = 0
        self.alive = False
        return self.alive


class WeaponsAbstract(models.Model):

    sword = models.IntegerField(default=10, blank=True, null=True)

    class Meta:
        abstract = True

    def activate_extra_damage(self, weapon):
        self.damage += int(weapon)
        return self.damage

    def deactivate_extra_damage(self, weapon):
        self.damage -= int(weapon)
        return self.damage


class Knight(ScoreAbstract, WeaponsAbstract):

    def __int__(self):
        return self.id


class Archer(ScoreAbstract, WeaponsAbstract):

    def __int__(self):
        return self.id


class Catapult(ScoreAbstract):

    def __int__(self):
        return self.id


class Army(models.Model):

    knights = models.ManyToManyField(
                        Knight,
                        blank=True,
                        related_name='knights')

    archers = models.ManyToManyField(
                        Archer,
                        blank=True,
                        related_name='archers')

    catapults = models.ManyToManyField(
                        Catapult,
                        blank=True,
                        related_name='catapults')

    armyAdd = models.OneToOneField(
                        'self',
                        blank=True,
                        null=True,
                        related_name='army_add',
                        on_delete=models.SET_NULL
                    )



    def __int__(self):
        return self.id
