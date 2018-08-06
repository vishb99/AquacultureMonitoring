import pandas as pd


def transform_data(in_file, out_file):
    input_file = pd.read_csv(in_file)
    print(input_file.shape)
    vessel_types_needed = [30, 1001, 1002]

    not_null_columns = ['MMSI', 'LAT', 'LON', 'BaseDateTime']
    not_needed_statuses = ['at anchor']

    # output_df = input_file.loc[input_file['VesselType'].isin(vessel_types_needed)]
    # output_df = output_df.loc[~output_df['Status'].isin(not_needed_statuses)]
    # df[cols] = df[df[cols] > 0][cols]
    input_file = input_file.loc[input_file['LAT'] > 42.70307]
    print(input_file.shape)
    input_file = input_file.loc[input_file['LAT'] < 45.10885]
    print(input_file.shape)
    input_file = input_file.loc[input_file['LON'] < -60.83896]
    print(input_file.shape)
    input_file = input_file.loc[input_file['LON'] > -64.83798]
    print(input_file.shape)

    # output_df.dropna(subset=not_null_columns)

    # print(output_df.shape)

    input_file.to_csv(out_file)


transform_data("xaa.csv", "xaa_transformed4.csv")

