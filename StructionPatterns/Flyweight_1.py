# class Bullet:
#     def __init__(self, x, y, z, velocity):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.velocity = velocity
#         self.asset = '▆▆▶'

class BulletContext:
    def __init__(self, x, y, z, velocity, visible):
        self.x = x
        self.y = y
        self.z = z
        self.visible = visible
        self.velocity = velocity
        
class BulletFlyweight:
    def __init__(self):
        self.asset = '▆▆▶'
        self.bullets = []
        
    def bullet_factory(self, x, y, z, velocity):
        bull = [b for b in self.bullets if b.x==x and b.y==y and b.z==z and b.velocity==velocity]
        if not bull:
            bull = BulletContext(x,y,z,velocity)
            self.bullets.append(bull)
        else:
            bull = bull[0]
            
        return bull
    
    # def move(self, bull):
        
        
    def print_bullets(self):
        print('Bullets:')
        for bullet in self.bullets:
            print(str(bullet.x)+' '+str(bullet.y)+' '+str(bullet.z)+' '+str(bullet.velocity))


if __name__ == '__main__':

    bf = BulletFlyweight()
    # Добавляем пули
    bf.bullet_factory(1,1,1,1)
    bf.bullet_factory(1,2,5,1)
    bf.print_bullets()

    # Добавляем уже существующую пулю
    bf.bullet_factory(1,1,1,1)
    bf.print_bullets()