

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(a) - 1):
            for j in range(i + 1,len(a)):
                if abs(a[i] - a[j]) > self.maximumDifference:
                    self.maximumDifference = abs(a[i] - a[j])

