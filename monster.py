import random


class Monster:
    monster_types = {
        "초급": ["고블린", "스켈레톤", "좀비", "오크", "슬라임"],
        "중급": ["트롤", "웨어울프", "마미라", "미노타우르스", "하피"],
        "고급": ["뱀파이어", "걸렘", "데몬", "드래곤", "벨벳"]
    }

    def __init__(self, stage):
        self.stage = stage
        self.type = self.get_monster_type()
        self.hp = 10 + 5 * stage
        self._str = 1 + 2 * stage
        self.level = stage

    def get_monster_type(self):
        # 스테이지에 맞는 몬스터 등급을 선정하고, 해당 등급에서 랜덤한 몬스터 선택
        if self.stage < 5:
            monster_level = "초급"
        elif self.stage < 8:
            monster_level = "중급"
        else:
            monster_level = "고급"

        return random.choice(Monster.monster_types[monster_level])

    def attack_player(self, player):
        damage = self._str - player.defense
        if damage < 0:
            damage = 0
        player.hp -= damage
        print(f"{self.type}이(가) {player.name}에게 {damage}의 피해를 입혔습니다.")


class MonsterGenerator:
    def __init__(self, stage):
        self.stage = stage
        self.monsters = self.generate_monsters()

    def generate_monsters(self):
        # 스테이지별 몬스터 수 범위 설정
        min_monsters = max(1, self.stage - 2)
        max_monsters = min(10, self.stage + 2)

        # 스테이지별 몬스터 등급 및 랜덤한 수의 몬스터 생성
        if self.stage < 5:
            monster_levels = ["초급"] * max_monsters
        elif self.stage < 8:
            monster_levels = ["초급", "중급"] * \
                (max_monsters // 2) + ["초급"] * (max_monsters % 2)
        else:
            monster_levels = ["초급", "중급", "고급"] * (max_monsters // 3) + ["초급", "중급"] * (
                (max_monsters % 3) // 2) + ["초급"] * ((max_monsters % 3) % 2)

        monsters = [Monster(self.stage) for level in monster_levels]

        return monsters


# 스테이지 3 몬스터 출력
def stage_monster(stage):
    monsters = []
    generator = MonsterGenerator(stage)
    for i, monster in enumerate(generator.monsters):
        # print(f"{i+1}. {monster.type} (Lv.{monster.level})")
        monsters.append(monster)
    return monsters
