import numpy as np
import pandas as pd

def engineer_nids_features(df: pd.DataFrame) -> pd.DataFrame:
    """Applies robust domain feature engineering to raw telemetry."""
    df_out = df.copy()
    
    # 1. Byte transfer asymmetry ratio
    df_out['bytes_ratio'] = (df_out['src_bytes'] + 1.0) / (df_out['dst_bytes'] + 1.0)
    
    # 2. Log transform heavy-tailed distributions
    df_out['log_src_bytes'] = np.log1p(df_out['src_bytes'])
    df_out['log_dst_bytes'] = np.log1p(df_out['dst_bytes'])
    df_out['log_duration'] = np.log1p(df_out['duration'])
    
    # 3. Compound host and service-level SYN error rate
    df_out['total_serror'] = (df_out['serror_rate'] + df_out['srv_serror_rate']) / 2.0
    
    # 4. Bin low frequency port applications to protect against dimensionality explosion
    top_services = ['http', 'private', 'domain_u', 'smtp', 'ftp_data']
    df_out['service_binned'] = df_out['service'].apply(lambda x: x if x in top_services else 'other')
    
    return df_out
