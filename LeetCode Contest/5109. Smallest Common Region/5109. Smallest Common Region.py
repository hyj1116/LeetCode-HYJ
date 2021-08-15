import random


class Solution:
    def findSmallestRegion(self, regions, region1, region2):
        for i in regions:
            if region1 in i and region2 in i:
                return i[0]
        region1_parent_index, region1_parent_value = self.findRegionParent(regions,region1)
        region2_parent_index, region2_parent_value = self.findRegionParent(regions,region2)
        while region1_parent_value != region2_parent_value:
            if region1_parent_value == region2:
                return region2
            if region2_parent_value == region1:
                return region1
            if region1_parent_index > region2_parent_index:
                region1_parent_index, region1_parent_value = self.findRegionParent(regions,region1_parent_value)
            if region2_parent_index > region1_parent_index:
                region2_parent_index, region2_parent_value = self.findRegionParent(regions,region2_parent_value)
        return region1_parent_value
    def findRegionParent(self, regions,region):
        for i in range(len(regions)):
            if region in regions[i] and regions[i].index(region) != 0:
                return i, regions[i][0]


if __name__ == "__main__":
    solution = Solution()
    regions= [["zDkA","GfAj","lt"],["GfAj","rtupD","og","l"],["rtupD","IT","jGcew","ZwFqF"],["og","yVobt","EjA","piUyQ"],["IT","XFlc","W","rB"],["l","GwQg","shco","Dub","KwgZq"],["jGcew","KH","lbW"],["KH","BZ","sauG"],["yVobt","Aa","lJRmv"],["BZ","v","zh","oGg","WP"],["XFlc","Sn","ftXOZ"],["sauG","If","nK","HHOr","yEH","YWMgF"],["GwQg","Mfb","gr","S","nQ"],["shco","xsUkW"],["xsUkW","Cssa","TgPi","qx"],["v","SAH","Rjr"],["lt","Q","fWB","a","Wk","zpqU"],["If","e","y","quEA","sNyV"],["piUyQ","G","aTi"],["Sn","rVIh","twv","pYA","Ywm"],["zh","PWeEf"],["Mfb","GEs","XjpeC","p"],["GEs","oXMG","tNJYJ"],["SAH","bmFhM"],["bmFhM","SOvB","RWsEM","z"],["SOvB","iD","pLGYN","Zqk"],["Dub","PnGPY"],["a","TekG","zp"],["XjpeC","vK","aaO","D"],["pLGYN","ldb"],["oGg","x"],["nQ","IOw"],["Aa","wmYF"],["Zqk","th"],["ZwFqF","GDl"],["th","JyOSt","ALlyw"],["lbW","M"],["yEH","UY","GIwLp"],["JyOSt","i"],["x","dclJ"],["wmYF","xreBK"],["PnGPY","Ev","lI"],["ALlyw","jguyA","Mi"],["oXMG","uqe"],["sNyV","WbrP"]]
    region1="RWsEM"
    region2="GfAj"
    print(solution.findSmallestRegion(regions, region1, region2))
