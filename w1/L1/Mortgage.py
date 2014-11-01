def findPayment(loan, r, m):
    """
    Assumes: loan and r are floats, m an int
    returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months
    """
    # according http://www.mtgprofessor.com/formulas.htm
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage(object):

    """
    Abstract class for building different kinds of mortgages
    """

    def __init__(self, loan, annRate, months):
        """create a new mortgage"""
        self.loan = loan
        self.rate = annRate / 12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None  # description of mortgage

    def makePayment(self):
        """make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """return the totoal amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    # fixed-rate mortgage

    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r * 100) + '%'


class FixedWithPts(Fixed):
    # fixed-rate  mortgage with up-front points

    def __init__(self, loan, r, months, pts):
        Fixed.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100.0)]
        self.legend += ', ' + str(pts) + ' points'


class TwoRate(Mortgage):
    # mortgage that chnages interest rate after 48 months

    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12.0
        self.legend = str(teaserRate * 100) + "% for " + \
            str(self.teaserMonths) + ' months, then ' + str(r * 100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate, self.months -
                                       self.teaserMonths)
        Mortgage.makePayment(self)


def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2,
                     varMoths):
    # helper function to try out alternatives
    # create alternative mortgages
    totMonths = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMoths)
    morts = [fixed1, fixed2, twoRate]
    # run experiment
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    # report result
    for m in morts:
        print(m)
        print("  Total payments = $" + str(int(m.getTotalPaid())))


# amount borrowed: $200,000
# term: 30 years
# option 1: rate = 7%
# option 2: 3.25 points upfront, rate = 5%
# option 3: 48 months of rate 5 %, then rate = 9.5%

compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25,
                 ptsRate=0.05, varRate1=0.05, varRate2=0.095, varMoths=48)
