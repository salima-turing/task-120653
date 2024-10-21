import unittest
import pandas as pd
from collections import Counter
import random, string


# Dummy data for structured data
structured_data = pd.DataFrame({
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
	'Age': [25, 30, 35, 40, 28],
	'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'emma@example.com'],
	'Location': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'Paris']
})


def anonymize_structured_data_gdpr(df, k=3):
	"""
	Dummy GDPR-compliant anonymization function for structured data.
	Ensures k-anonymity for certain columns.
	"""
	df['Name'] = df['Name'].apply(lambda x: ''.join(random.choice(string.ascii_lowercase) for _ in range(6)))
	df['Email'] = df['Email'].apply(lambda x: ''.join(random.choice(string.ascii_lowercase) for _ in range(10)))

	# Ensure k-anonymity for 'Age' and 'Location' columns
	for col in ['Age', 'Location']:
		value_counts = Counter(df[col])
		for val, count in value_counts.items():
			if count < k:
				df.loc[df[col] == val, col] = random.choice(list(value_counts.keys()))

	return df


class TestAnonymizationGDPR(unittest.TestCase):

	def test_anonymize_structured_data_gdpr(self):
		"""Test GDPR-compliant anonymization of structured data"""
		anonymized_df = anonymize_structured_data_gdpr(structured_data.copy(), k=3)

		# Check k-anonymity for 'Age' and 'Location' columns
		for col in ['Age', 'Location']:
			value_counts = Counter(anonymized_df[col])
			self.assertTrue(all(count >= 3 for count in value_counts.values()), f"Column '{col}' does not meet k-anonymity")

		# Check if other columns are anonymized
		self.assertTrue(all(len(name) == 6 for name in anonymized_df['Name']))
		self.assertTrue(all(len(email) == 10 for email in anonymized_df['Email']))

		# Preserve some data utility by checking for preserved frequency distributions
		original_freq = structured_data['Location'].value_counts()
		anonymized_freq = anonymized_df['Location'].value_counts()
		self.assertTrue(abs(original_freq - anonymized_freq).sum() <= 1, "Frequency distributions changed too much")

if __name__ == '__main__':
	unittest.main()
