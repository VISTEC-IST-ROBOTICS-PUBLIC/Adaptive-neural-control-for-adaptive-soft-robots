import numpy as np
class Learning:
    """
    Neural learning module based on recurrent synaptic plasticity.

    Attributes:
    - st_prev: float, previous synaptic state (default is 0.0).
    - W_R: float, the current weight value to be updated.
    - W_recall: float, recall weight factor (default is 0.01).
    - W_forgot: float, forgetting weight factor (default is 0.01).

    Methods:
    - compute_Re: Static method to compute the state neuron R_e based on the prediction error.
    - calculate: Calculates the output neuron value (Ro) and updates internal state.
    """
   
    def __init__(self, W_recall=0.01, W_forgot=0.01):
        """
        Initialize the Learning module.

        Parameters:
        - W_R: float, the current weight value to be updated.
        - W_recall: float, recall weight factor (default is 0.01).
        - W_forgot: float, forgetting weight factor (default is 0.01).
        """
        self.st_prev = 0.0
        self.W_recall = W_recall
        self.W_forgot = W_forgot

    @staticmethod
    def compute_Re(error):
        """
        Compute the state neuron R_e based on the prediction error.

        Parameters:
        - error: float, the prediction error e(t).

        Returns:
        - Re: float, the state neuron value.
        """
        if  abs(error) >= 0.05:
            return 10
        else:
            return 1

    def calculate(self, laser, error):
        """
        Perform the learning calculation.

        Parameters:
        - laser: float, the normalized laser input data.
        - error: float, the prediction error e(t).

        Returns:
        - Ro: float, the output neuron value.
        """
        # Compute the state neuron R_e based on the prediction error
        Re = self.compute_Re(error)

        # Calculate the recurrent synaptic plasticity update
        st = self.st_prev + (self.W_recall * laser * Rm) + (self.W_forgot * (laser - 1) * (self.st_prev**2))

        # Compute Rm
        Rm = st + laser

        # Calculate the output neuron Ro
        Ro = 0.05 * Re + np.tanh(Rm) * 0.1

        # Update internal state
        self.st_prev = st

        return Ro
