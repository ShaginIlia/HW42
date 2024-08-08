import unittest
import test_HW41
import Test_HW40

run_tourST = unittest.TestSuite()
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_HW41.TournamentTest))
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_HW40.RunnerTest))
# runnerST = unittest.TestSuite()
# runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_HW40.RunnerTest))

# run = unittest.TextTestRunner(verbosity=2)
# run.run(runnerST)
run2 = unittest.TextTestRunner(verbosity=2)
run2.run(run_tourST)
