from mrjob.job import MRJob
from mrjob.step import MRStep

class AnimalCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_animal,
                   reducer=self.reducer_count_animal)
        ]

    def mapper_get_animal(self, _, line):
        word = line.strip()    
        yield word, 1

    def reducer_count_animal(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    AnimalCount.run()