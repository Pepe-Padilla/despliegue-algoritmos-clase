from playground import load_dataset, mlflow_tracking, data_treatment

def main():
  print("Eejcutamos el main")

  df = load_dataset()
  x_train, x_test, y_train, y_test = data_treatment(df)
  mlflow_tracking('patata', x_train, x_test, y_train, y_test, [1,2,3,45])

if __name__ == '__main__': 
  main()