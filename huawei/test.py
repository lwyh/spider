def consecutive_sequences(days):
        sequences=[]
        current_sequence=[days[0]]
        for i in range(1,len(days)):
            if(days[i]==days[i-1]+1):
                current_sequence.append(days[i])
            else:
                if(len(current_sequence)>1):
                    sequences.append((current_sequence[0],current_sequence[-1],len(current_sequence)))
                    current_sequence=[days[i]]
            print(current_sequence)

                
        #追加最后一个连续序列
        if(len(current_sequence)>1):
            sequences.append((current_sequence[0],current_sequence[-1],len(current_sequence)))

        print(sequences)
        return sequences
if __name__ == '__main__':

    consecutive_sequences([15,16,17,18,19])
