class Ui(object):
    def __init__(self,ctrl):
        self.ctrl=ctrl

    def gradientDescent(self):
        array=self.ctrl.callMainForGradientDescentRegressionProblem()
        best_error=array[0]
        coeffs=array[1]
        print("Best Error:"+str(best_error))
        print("Found function:  "+str(round(coeffs[0],2))+"*x^5 + "+str(round(coeffs[1],2))+"*x^4 + "+str(round(coeffs[2],2))+"*x^3 + "+str(round(coeffs[3],2))+"*x^2 + "+str(round(coeffs[4],2))+"*x + "+str(round(coeffs[5],2)))



