#9. *Key Revolver
#Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission. 
#He needs to unlock a safe locked by several locks in a row, which all have varying sizes.
#The hero possesses a special weapon called the Key Revolver, with special bullets. 
#Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. 
#The bullet goes into the keyhole, then explodes, completely destroying it. 
#Sam doesn't know the size of the locks, so he needs to just shoot at all of them until the safe runs out of locks.
#What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, keeps his top-secret Georgian Chacha Brandy recipe inside. 
#It's valued differently across different times of the year, so Sam's boss will tell him what it's worth over the radio. 
#One last thing, every bullet Sam fires will also cost him money, which will be deducted from his pay from the price of the intelligence.
#Good luck, operative.

from collections import deque

bullet_price = int(input())
mag_max = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

mag = mag_max
bullets_shot = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    mag -= 1
    bullets_shot += 1

    if mag == 0 and bullets:
        mag = mag_max if len(bullets) > mag_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((bullets_shot * bullet_price) - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
