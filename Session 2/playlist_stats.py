"""
Session 2 - Task 1: Spotify Playlist Daily Plays Statistics
------------------------------------------------------------
Script name: playlist_stats.py

Calculates the mean (average) number of daily song plays
for a Spotify playlist from a given list of play counts.
"""

import statistics


def calculate_playlist_mean(play_counts):
    """
    Takes a list of daily Spotify song play counts and calculates
    the mean (average) number of plays.
    """
    if not play_counts:
        return 0.0
    
    total_plays = sum(play_counts)
    total_days = len(play_counts)
    mean_plays = total_plays / total_days
    return mean_plays


def main():
    # Example daily play counts from Task 1
    daily_plays = [120, 135, 150, 200, 120, 90, 200]

    print("=" * 60)
    print("SESSION 2 - TASK 1: PLAYLIST DAILY PLAY STATS")
    print("=" * 60)
    print(f"Daily Spotify Play Counts: {daily_plays}")
    print(f"Total Days Monitored:      {len(daily_plays)}")
    print(f"Total Number of Plays:     {sum(daily_plays)}")

    # Method 1: Manual arithmetic mean (sum / count)
    mean_manual = calculate_playlist_mean(daily_plays)
    print(f"\nMean (Manual Calculation): {mean_manual:.2f} plays/day")

    # Method 2: Python's built-in statistics module
    mean_stat = statistics.mean(daily_plays)
    print(f"Mean (statistics.mean):    {mean_stat:.2f} plays/day")
    print("=" * 60)


if __name__ == "__main__":
    main()
