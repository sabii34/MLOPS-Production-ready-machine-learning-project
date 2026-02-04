from us_visa.pipline.training_pipeline import TrainPipeline

def main():
	obj = TrainPipeline()
	obj.run_pipeline()
	data_ingestion_artifact = obj.start_data_ingestion()
	print(data_ingestion_artifact)
	return

if __name__ == "__main__":
	main()