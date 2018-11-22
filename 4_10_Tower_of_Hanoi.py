def moveTower(height,fromPole,toPole,withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        # ↑We move all but the bottom disk on the initial tower to an intermediate pole.
        moveDisk(fromPole,toPole)
        # moves the bottom disk to its final resting place.
        moveTower(height-1,withPole,toPole,fromPole)
        # move the tower from the intermediate pole to the top of the largest disk.


def moveDisk(fromPole,toPole):
    print('moving disk from',fromPole,'to',toPole)

print(moveTower(4,'A','B','C'))