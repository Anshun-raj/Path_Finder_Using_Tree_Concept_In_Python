class Main_path:
    lis1=[]
    dest="Railway_Station"
    def __init__(self,path):
        self.path=path;
        self.child_path=[];
        self.initial_path=None;


    def get_level(self):
        level=0
        loc=self.initial_path
        while loc:
            level+=1
            loc=loc.initial_path

        return level

    def print_path(self):
        space=" "*self.get_level()*3
        direction=space+"|-->" if self.initial_path else ""
        print(direction+self.path)
        if self.child_path:
            for new_path in self.child_path:
                new_path.print_path()

    def add_path(self,new_path):
        new_path.initial_path=self
        Main_path.lis1.append(new_path)
        self.child_path.append(new_path)

    def get_path(self):
        for i in range(len(Main_path.lis1)):
            if Main_path.lis1[i] == Main_path.dest:
                print("You ca choose this path")
                break
        else:
            print("There is no route available for your destination")


def build_path():
    origin=Main_path("Banaras_Bank_chowk")

    durga_asthan=Main_path("Durga_Asthan");
    durga_asthan.add_path("Gola_Road")
    durga_asthan.add_path("Saraiyaganj_Tower")
    durga_asthan.add_path("Company_Bagh")
    durga_asthan.add_path("Railway_Station")

    pakki_sarai=Main_path("Pakki_Sarai")
    pakki_sarai.add_path("Hathi_Chowk")
    pakki_sarai.add_path("Miscort_Lane")
    pakki_sarai.add_path("Mithanpura_chowk")


    balu_ghat=Main_path("Balu_Ghat");
    balu_ghat.add_path("Akhara_Ghat");
    balu_ghat.add_path("Zero_Mile")
    balu_ghat.add_path("Skmch_Hospital");



    origin.add_path(durga_asthan)
    origin.add_path(pakki_sarai)
    origin.add_path(balu_ghat)

    origin.print_path()

    origin.get_path()


if __name__=='__main__':
    build_path()



