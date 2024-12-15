

# Step 1: Load the data
# Replace this with the actual path to your dataset
data = pd.read_csv("data.csv")

# Step 2: Ensure proper timestamp formatting and sorting
data['timestamp'] = pd.to_datetime(data['TIMESTAMP'])
data = data.sort_values(by='timestamp')

# Step 3: Calculate basic features
data['MIDPOINT'] = (data['LAST_ASK'] + data['LAST_BID']) / 2
data['PCT_CHANGE'] = data['MIDPOINT'].pct_change()
data['ROLLING_MEAN'] = data['MIDPOINT'].rolling(window=10).mean()
data['ROLLING_STD'] = data['MIDPOINT'].rolling(window=10).std()
data['ROLLING_MAX'] = data['MIDPOINT'].rolling(window=10).max()
data['ROLLING_MIN'] = data['MIDPOINT'].rolling(window=10).min()
data['BOLLINGER_UPPER'] = data['ROLLING_MEAN'] + 2 * data
