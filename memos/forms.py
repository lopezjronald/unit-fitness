from django import forms


class ExemptionForm(forms.Form):
    RANK_CHOICES = [
        ("AB", "AB"),
        ("AMN", "AMN"),
        ("A1C", "A1C"),
        ("SrA", "SrA"),
        ("SSgt", "SSgt"),
        ("TSgt", "TSgt"),
        ("MSgt", "MSgt"),
        ("SMSgt", "SMSgt"),
        ("CMSgt", "CMSgt"),
        ("2Lt", "2Lt"),
        ("1Lt", "1Lt"),
        ("Capt", "Capt"),
        ("Maj", "Maj"),
        ("Lt Col", "Ll Col"),
        ("Col", "Col"),
        ("Brig Gen", "Brig Gen"),
        ("Maj Gen", "Maj Gen"),
        ("Lt Gen", "Lt Gen"),
        ("General", "General"),
    ]

    TYPE_CHOICES = [
        ("Commander", "Commander"),
        ("Medical", "Medical"),
        ("Pregnancy", "Pregnancy"),
        ("Medical", "Medical"),
    ]

    FITNESS_STATUS_CHOICES = [
        ("Excellent", "Excellent"),
        ("Satisfactory", "Satisfactory"),
        ("Unsatisfactory", "Unsatisfactory"),
        ("Composite Exemption", "Composite Exemption"),
    ]

    type = forms.ChoiceField(label="Exemption Type", choices=TYPE_CHOICES, required=True)
    current_date = forms.DateField(label="Today's Date", required=True, widget=forms.SelectDateWidget())
    member_rank = forms.ChoiceField(label="Member's Rank", choices=RANK_CHOICES, required=True)
    member_first_name = forms.CharField(label="Member's First Name", max_length=50, required=True)
    member_middle_name = forms.CharField(label="Member's Middle Name", max_length=50)
    member_last_name = forms.CharField(label="Member's Last Name", max_length=50, required=True)
    dod_number = forms.IntegerField(label="DOD Number", required=True)
    start_date = forms.DateField(label="Start Date", required=True, widget=forms.SelectDateWidget())
    end_date = forms.DateField(label="End Date", required=True, widget=forms.SelectDateWidget())
    current_fitness_status = forms.ChoiceField(label="Current Fitness", choices=FITNESS_STATUS_CHOICES, required=True)
    documentation = forms.BooleanField(label="AF Form 469/422 Included?", initial=False)
    reason = forms.CharField(label="Reason for Unsatisfactory Score", widget=forms.Textarea, required=True)
    ufpm_rank = forms.ChoiceField(label="UFPM Rank", choices=RANK_CHOICES, required=True)
    ufpm_first_name = forms.CharField(label="UFPM First Name", max_length=50, required=True)
    ufpm_last_name = forms.CharField(label="UFPM Last Name", max_length=50, required=True)
    ufpm_email = forms.EmailField(label="UFPM's Email", required=True)
    ufpm_phone = forms.CharField(label="UFPM's Phone Number", max_length=20, initial="707-424-3406")
    commander_rank = forms.ChoiceField(label="Commander's Rank", choices=RANK_CHOICES, required=True)
    commander_first_name = forms.CharField(label="Commander's First Name", max_length=50, required=True)
    commander_last_name = forms.CharField(label="Commander's Last Name", max_length=50, required=True)
