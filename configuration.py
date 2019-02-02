class Configuration:
    """
    configurations.py
    -----------------
    A class designed to represent an instance of the application's settings
    Contains data such as game information, file paths, character resources, etc.
    """


    # Class Variables #
    outfile_prefix = 'output/config_'
    img_dir = 'res/img/config_'



    def __init__(self):
        """
        Default Constructor for the class
        All data members are set to default values
        """
        # Member Variables
        self.id = 0
        self.config_name = 'default'
        self.game_name = 'ssbm'
        self.p1_tag_outfile = 'p1.txt'
        self.p2_tag_outfile = 'p2.txt'
        self.p1_games_outfile = 'p1_games.txt'
        self.p2_games_outfile = 'p2_games.txt'
        self.p1_char_outfile = 'p1_char.png'
        self.p2_char_outfile = 'p2_char.png'

        # Data Structures
        # initialize header dict with default values
        #       Dictionary is organized as: {field title: output file name}
        self.header_fields = {'Main Header': 'header.txt',
                              "Subheader": "subheader.txt"}

        # Initialize the character list
        #       Characters are to be stored as:
        #           [ [name, icon, image source file], [...], ... ]
        self.characters = []



    # Parametized constructor
    # def __init__(self, file):
    #     """
    #
    #     :param file: The input file for the object
    #     I actually don't know if we'll ever use this constructor, lol
    #     """



    def get_name(self):
        return self.game_name

    def get_output_path(self):
        return outfile_prefix + str(self.id)

    def get_images_path(self):
        return img_dir + str(self.id)


    def save(self, outfile):
        """

        :param outfile: The path for the output file
            We actually might not even need this lol
            We have the right file paths already, so...
        :return: success, maybe? lol idk
        """
        pass