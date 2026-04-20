import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_lst = []
    tot_score = 0
    for i in sys.argv[1:]:
        try:
            score_lst.append(int(i))
            tot_score += int(i)
        except ValueError:
            print(f"Invalid parameter : '{i}'")
    if len(score_lst) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score_lst}")
        print(f"Total players: {len(score_lst)}")
        print(f"Total score: {tot_score}")
        print(f"Average score: {tot_score/len(score_lst)}")
        print(f"High score: {max(score_lst)}")
        print(f"Low score: {min(score_lst)}")
        print(f"Score range: {max(score_lst) - min(score_lst)}")