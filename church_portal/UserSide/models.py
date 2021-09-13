from django.db import models
from accounts.models import Customusers
from AdminSide.models import sermon
from .paystack import PayStack

# Create your models here.

class family(models.Model):
    who = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="the_user", blank=True,null=True)
    gfather = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="grand_father",blank=True,null=True)
    gmother = models.ForeignKey(Customusers,on_delete=models.CASCADE , related_name="grand_mother",blank=True,null=True)
    father = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="father",blank=True,null=True)
    mother = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="mother",blank=True,null=True)
    spouse = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="spouse",blank=True,null=True)
    child = models.ForeignKey(Customusers,on_delete=models.CASCADE, related_name="child",blank=True,null=True)

    def __str__(self):
        return self.who.username

    # gfather = models.CharField(max_length=200, null=True, blank=True)
    # gmother = models.CharField(max_length=200, null=True, blank=True)
    # father = models.CharField(max_length=200, blank=True,null=True)
    # mother = models.CharField(max_length=200, null=True, blank=True)
    # spouse = models.CharField(max_length=200, null=True, blank=True)
    # child = models.CharField(max_length=200, null=True, blank=True)
    



class comment(models.Model):
    by = models.ForeignKey(Customusers, on_delete=models.CASCADE)
    cfor = models.ForeignKey(sermon,on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.by.username





class Payment(models.Model):
    fname = models.CharField(max_length=200, null=True, blank=True)
    lname = models.CharField(max_length=200, null=True, blank=True)
    amount = models.PositiveIntegerField()
    email = models.EmailField()
    ref = models.CharField(max_length=200)
    status = models.CharField(max_length=200,null=True,blank=True)
    channel = models.CharField(max_length=200,null=True,blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname



    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref,self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
                self.channel = result['channel']
                self.status = result['status']
            self.save()
        if self.verified:
                return True, result['amount']
        return False

    # #generating random reference on save
    # def save(self, *args, **kwargs) -> None:
    #     while not self.ref:
    #         ref = secrets.token_urlsafe(50)
    #         similar_ref = Payment.objects.filter(ref=ref)
    #         if not similar_ref:
    #             self.ref = ref
    #     super().save(*args, **kwargs)

    
    #multiplying the amout receive by 100
    #a requirement in using paystack api
    # def amount_value(self) -> int:
    #     return self.amount * 100