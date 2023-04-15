class Cube:
    ''' A class representing a cube '''
    def __init__(self, side_length):
        ''' 
        Initialize a new cube with the given sides length 
        Args:
            side_length (float): The lengtf of each side of the cube
        '''
        self.side_length = side_length

    def ask_values(self):
        self.side_length = int(input('Enter the length in mts here : '))
        
    
    def calculate_volume(self):
        '''
        Calculates the volume of the cube.
        Returns:
            float: The volumn of the cube
        '''
        return self.side_length ** 3

cube = Cube(0)
cube.ask_values()
print(f'Volume: {cube.calculate_volume()} mts3')