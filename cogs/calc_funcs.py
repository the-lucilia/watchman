import math as ma


def InfCalc(days: float, endorsements: int, current: int):
    """Days, Endorsements, Current Influence."""
    return  (2 * endorsements * days) + (2 * days) + current


def EndoCalc(influence: int, days: float, current: int):
    """Influence, Days, Current Influence."""
    return ((influence - current) / (2 * days)) - 1


def DayCalc(endorsements: int, influence: int, current: int):
    """Endorsements, Influence, Current Influence."""
    return  (influence - current) / (2 * endorsements + 2)


def RoBan(t_current: int, current: int, t_endorsements: int, endorsements: int):
    """Target's Current Influence, Officer's Current Influence, Target's Endorsements, Officer's Endorsements."""
    return (t_current - current) / (2 * t_endorsements - 2 * endorsements)


def DelBan(t_current: int, current: int, t_endorsements: int, endorsements: int):
    """Target's Current Influence, Delegate's Current Influence, Target's Endorsements, Delegate's Endorsements."""
    return  (t_current - 2 * current) / (-2 * t_endorsements + 4 * endorsements + 2)


def StabDecay(stable: int):
    """Desired stabilized influence."""
    return ma.ceil(stable / 360) - 1


def EndoDecay(endorsements: int):
    """Target nation's endorsements."""
    return 360 * endorsements + 360


def StrongholdCalc(numwa: int, nonwa: int):
    """WA Nations, Non WA Nations."""
    if nonwa >= 200:
        nonwa_cost = 4000
    else:
        nonwa_cost = nonwa * 20
    return (numwa * 80) + nonwa_cost


def PasswordCalc(numnat: int):
    return numnat * 40
