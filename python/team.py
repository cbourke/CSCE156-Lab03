

class Team:
    """
    Models a Major League Baseball team using its name, wins and losses
    """

    def __init__(self, name, wins, loss):
        self.name = name
        self.wins = wins
        self.loss = loss

    def getWinPercentage(self):
        return self.wins / (self.wins + self.loss) * 100

    def __str__(self):
        return f"{self.name:10} ({self.getWinPercentage():.2f})"
