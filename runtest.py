#in this file we shall test bottles.py
import unittest
import bottles

class tests (unittest.TestCase):
    def test1(self):
        song_expected_last_word = 'floor'
        song_actual_last_word = bottles.song[-5:]
        self.assertEquals(song_expected_last_word, song_actual_last_word, "last word is wrong, Test 1 fails")

def test2(self):
    index_of_10 = bottles.song.index('10')
    index_of_9 = bottles.song.index('9')
    index_of_5 = bottles.song.index('5')
    index_of_4 = bottles.song.index('4')
    assert index_of_10 < index_of_9 #"10 does not come before 9, Test 2 fails"
    assert index_of_5 > index_of_9 #"5 does not come after 9, Test 2 fails"
    assert index_of_5 < index_of_4 #"5 does not come before 5, Test 2 fails"

def test3(self):
    assert (' 0' in bottles.song) #0 is not in bottles.song, test 3 fails 
    
if __name__ == '__main__':
    unittest.main()
