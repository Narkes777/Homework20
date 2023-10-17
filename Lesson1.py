import time
import threading

def create_file_with_delay(filename):
    with open(filename, 'w') as file:
        file.write("Содержимое файла")

    time.sleep(1)

start_time = time.time()

for i in range(100):
    filename = f"file_{i}.txt"
    create_file_with_delay(filename)
    print(f"Создан файл: {filename}")

end_time = time.time()

print(f"Время выполнения без многопоточности: {end_time - start_time} секунд")

start_time = time.time()

threads = []
for i in range(100):
    filename = f"file_thread_{i}.txt"
    thread = threading.Thread(target=create_file_with_delay, args=(filename,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Время выполнения с многопоточностью: {end_time - start_time} секунд")
