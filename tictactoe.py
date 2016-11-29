#TicTacToe
#myfunproject

import random

class BadInputError(Exception):
    pass

class LogicError(Exception):
    pass

#===========GAMEBOARDS===========#

blankBoard = {
    'UL' : ' ', 'UM' : ' ', 'UR' : ' ',
    'CL' : ' ', 'CM' : ' ', 'CR' : ' ',
    'BL' : ' ', 'BM' : ' ', 'BR' : ' ',
}

debugBoard = {
    'UL' : ' ', 'UM' : ' ', 'UR' : ' ',
    'CL' : ' ', 'CM' : ' ', 'CR' : ' ',
    'BL' : ' ', 'BM' : ' ', 'BR' : ' ',
}

invertedSpaces = {
    'LU' : 'UL', 'MU' : 'UM', 'RU' : 'UR',
    'LC' : 'CL', 'MC' : 'CM', 'RC' : 'CR',
    'LB' : 'BL', 'MB' : 'BM', 'RB' : 'BR',
}

#===========DEFINITIONS===========#

'''Spaces'''
spaces = ('UL','UM','UR','CL','CM','CR','BL','BM','BR')

'''Wins'''
oWin = ('O','O','O')
xWin = ('X','X','X')

'''Doubles'''
oDoubles = [(' ','O','O'),('O',' ','O'),('O','O',' ')]
xDoubles = [(' ','X','X'),('X',' ','X'),('X','X',' ')]

'''Input'''
possibleInput = [key for key in blankBoard]
for key in invertedSpaces:
    possibleInput.append(key)
    
'''Space Types'''
corners = ('UL','UR','BL','BR')
sides = ('CL','CR', 'UM', 'BM')

'''Space Inversions'''

horizontalFlip = {
    'UL' : 'UR','UR' : 'UL',
    'CL' : 'CR','CR' : 'CL',
    'BL' : 'BR','BR' : 'BL',
    }

verticalFlip = {
    'UL' : 'BL', 'UM' : 'BM', 'UR' : 'BR',
    'BL' : 'UL', 'BM' : 'UM', 'BR' : 'UR',
    }

#===========OBJECTS===========#

class ticBoard():

    def __init__(self, mode='blank', copyBoard=None):
        if mode == 'blank':
            self.board = {space:blankBoard[space] for space in blankBoard}
        elif mode == 'debug':
            self.board = {space:debugBoard[space] for space in debugBoard}
        elif mode == 'copy' and copyBoard != None:
            self.board = {space:copyBoard.board[space] for space in copyBoard.board}
            
    def draw(self):
        '''Draw board'''
        print()
        print('    L   M   R ')
        print('U:  {} | {} | {} '.format(self.board['UL'], self.board['UM'], self.board['UR']))
        print('   -----------')
        print('C:  {} | {} | {} '.format(self.board['CL'], self.board['CM'], self.board['CR']))
        print('   -----------')
        print('B:  {} | {} | {} '.format(self.board['BL'], self.board['BM'], self.board['BR']))
        print()

    def place(self, symbol, space):
        '''Places a symbol at the designated space.'''
        try:
            self.board[space] = symbol
        except:
            raise BadInputError("{} is not a valid space for {}.".format(space, symbol))

    def clear(self):
        '''Clears board of all symbols.'''
        self.board = {space:' ' for space in self.board}

    def fieldReport(self):
        '''Returns dictionary of triads.'''
        report = {}
        report[('UL','UM','UR')] = (self.board['UL'],self.board['UM'],self.board['UR'])
        report[('CL','CM','CR')] = (self.board['CL'],self.board['CM'],self.board['CR'])
        report[('BL','BM','BR')] = (self.board['BL'],self.board['BM'],self.board['BR'])
        report[('UL','CL','BL')] = (self.board['UL'],self.board['CL'],self.board['BL'])
        report[('UM','CM','BM')] = (self.board['UM'],self.board['CM'],self.board['BM'])
        report[('UR','CR','BR')] = (self.board['UR'],self.board['CR'],self.board['BR'])
        report[('UL','CM','BR')] = (self.board['UL'],self.board['CM'],self.board['BR'])
        report[('UR','CM','BL')] = (self.board['UR'],self.board['CM'],self.board['BL'])
        return report

    def returnDoubles(self, report):
        '''Filters out report to only include triads close to winning. ie "[X,X, ]" or '[O, ,O]"'''
        doubles = {}
        for triad in report:
            if report[triad] in oDoubles or report[triad] in xDoubles:
                doubles[triad] = report[triad]
        return doubles
