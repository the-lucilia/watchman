import math as ma

class calc_funcs():
    def __init__(self, bot):
        self.bot = bot

    def InfCalc(self, days: float, endorsements: int, current: int):
        """Days, Endorsements, Current Influence."""
        return (2 * endorsements * days) + (2 * days) + current

    def EndoCalc(self, influence: int, days: float, current: int):
        """Influence, Days, Current Influence."""
        return ((influence - current) / (2 * days)) - 1

    def DayCalc(self, endorsements: int, influence: int, current: int):
        """Endorsements, Influence, Current Influence."""
        return (influence - current) / (2 * endorsements + 2)

    def RoBan(self, t_current: int, current: int, t_endorsements: int, endorsements: int):
        """Target's Current Influence, Officer's Current Influence, Target's Endorsements, Officer's Endorsements."""
        return (t_current - current) / (2 * t_endorsements - 2 * endorsements)

    def DelBan(self, t_current: int, current: int, t_endorsements: int, endorsements: int):
        """Target's Current Influence, Delegate's Current Influence, Target's Endorsements, Delegate's Endorsements."""
        return (t_current - 2 * current) / (-2 * t_endorsements + 4 * endorsements + 2)

    def StabDecay(self, stable: int):
        """Desired stabilized influence."""
        return ma.ceil(stable / 360) - 1

    def EndoDecay(self, endorsements: int):
        """Target nation's endorsements."""
        return 360 * endorsements + 360

    def StrongholdCalc(self, numwa: int, nonwa: int):
        """WA Nations, Non WA Nations."""
        if nonwa >= 200:
            nonwa_cost = 4000
        else:
            nonwa_cost = nonwa * 20
        return (numwa * 80) + nonwa_cost

    def PasswordCalc(numnat: int):
        return numnat * 40


async def setup(bot):
    await bot.add_cog(calc_funcs(bot))
