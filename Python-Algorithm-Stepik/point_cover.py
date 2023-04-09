import sys

def fetch_input():
    input_list = list(sys.stdin)
    
    segments_count = int(input_list[0])

    def process_coordinate_str(coordinate_str):
        coordinates = list(map(int, coordinate_str.split()))
        return coordinates

    segments_coordinates = list(
        map(process_coordinate_str, input_list[1:segments_count+1])
    )
    return segments_count, segments_coordinates

def main():
    
    segments_count, segments_coordinates = fetch_input()
    segments_coordinates.sort(key=lambda x: x[1])
    
    final_segments = []
    final_segments.append((segments_coordinates[0])[1])
    m = 0
    n = m + 1
    while m < (segments_count-1):
    #for m in range (0, segments_count):
        x1_end = (segments_coordinates[m])[1]
        #print('for x1_end:',x1_end)
        #for n in range (1, segments_count):
        x2_start = (segments_coordinates[n])[0]
        x2_end = (segments_coordinates[n])[1]

        #print('watch segment {}-{}'.format(x2_start,x2_end))
        if (x1_end >= x2_start) and (x1_end <= x2_end) : #если конец первого задевает последующие, проверяем следующий отрезок
            #print('x1_end= {} задевает последующие\n'.format(x1_end))
            m = m+1
        else:
            if  x1_end in final_segments:
                #print('уже в массиве')
                break
            else:
                #print('добавляем в массив \n')
                final_segments.append(x1_end)
                n = n + 1
                
    final_count = len(final_segments)   
    print(final_count)
    print(*final_segments)

    
if __name__ == "__main__":
    main()

