def read_separate_data(path, destination_name):
    with open(path,"r") as f:
        text = f.readlines();
        text=text[0].split("\t")
        with open(destination_name,"w") as writer:
            for line in text:
                writer.write(line+"\n")

read_separate_data("permissions.txt", "formatted_permissions.txt")
read_separate_data("receivers.txt", "formatted_receivers.txt")
read_separate_data("services.txt", "formatted_services.txt")