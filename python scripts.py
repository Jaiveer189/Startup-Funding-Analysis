{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8f52d9be",
   "metadata": {},
   "outputs": [],
   "source": [
    "BASE = Path(\"/mnt/data/Startup_Funding_Analysis\")\n",
    "DATA_DIR = BASE / \"data\"\n",
    "NOTEBOOKS_DIR = BASE / \"notebooks\"\n",
    "SCRIPTS_DIR = BASE / \"scripts\"\n",
    "DASH_DIR = BASE / \"dashboard\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "01569533",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Create directories\n",
    "for d in [BASE, DATA_DIR, NOTEBOOKS_DIR, SCRIPTS_DIR, DASH_DIR]:\n",
    "    d.mkdir(parents=True, exist_ok=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a6289662",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Copy the existing sample CSV into the data folder (if exists)\n",
    "sample_csv = Path(\"/mnt/data/startup_funding_sample.csv\")\n",
    "if sample_csv.exists():\n",
    "    shutil.copy(sample_csv, DATA_DIR / \"startup_funding_raw.csv\")\n",
    "else:\n",
    "    # If not present, create a tiny sample CSV as fallback\n",
    "    import pandas as pd\n",
    "    df = pd.DataFrame({\n",
    "        \"Startup Name\": [\"OYO\",\"Paytm\",\"Byju's\"],\n",
    "        \"Industry\": [\"Hospitality\",\"Fintech\",\"EdTech\"],\n",
    "        \"Investors\": [\"SoftBank\",\"Alibaba;Sequoia\",\"Tencent\"],\n",
    "        \"Funding Amount (Cr)\": [1500,1200,1000],\n",
    "        \"Location\": [\"Bangalore\",\"Noida\",\"Bangalore\"],\n",
    "        \"Date\": [\"2019-06-15\",\"2020-01-20\",\"2018-09-10\"]\n",
    "    })\n",
    "    df.to_csv(DATA_DIR / \"startup_funding_raw.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91e019aa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
