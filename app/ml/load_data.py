from datasets import load_dataset

def main():
    ds = load_dataset("kraina/airbnb", "all")
    print(ds)
    print("First row:", ds["train"][0])

if __name__ == "__main__":
    main()